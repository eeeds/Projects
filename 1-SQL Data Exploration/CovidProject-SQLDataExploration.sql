--Importing data and testing it.
/*
select * from coviddeaths c 
order by 3,4

select * from covidvaccinations c 
order by 3,4
*/

--Select Data what we are going to use
select "location" , "date" , total_cases , new_cases , total_deaths , population 
from coviddeaths c 
order by 1,2
--

--Looking at Total cases vs Total deaths 
--Shows likelihood of dying if you contract covid in your country
select "location" , "date" , total_cases , total_deaths , (total_deaths/total_cases)*100 as DeathPercentage
from coviddeaths c2 
where "location" like '%Para%'
order by 1,2

--Looking at total cases vs Population 
select "location" , "date" , population, total_cases , (total_deaths/population)*100 as CasesPercentage
from coviddeaths c2 
where "location" like '%Para%'
order by 1,2

--Looking at countries with Highest Infection Rate compared to Population
select "location" , population , max(total_cases) as highestInfectionCountry, 
max(cast(total_cases as decimal)/population)*100 as MaxCasesPercentage
from coviddeaths c2 
where population >0
group by "location", population
having max(total_cases)>0
order by maxcasespercentage desc 

--Showing countries with Hightest Death Count per Population

select "location" ,  max(total_deaths) as TotalDeathCount 
from coviddeaths c2 
where population >0 and continent  is not null
group by "location"
having max(total_deaths)>0
order by totaldeathcount desc 

--Let's break things down by continent

-- Showing continents with the highest death count per population

select continent, max(total_deaths) as TotalDeathCount
from coviddeaths c2 
where continent is not null 
group by continent 
order by totaldeathcount desc 

-- GLOBAL NUMBERS 

select  sum(new_cases ) as total_cases, sum(new_deaths ) as total_deaths,
100*(cast(sum(new_deaths) as decimal)/sum(new_cases)) as DeathPercentage
from coviddeaths c2 
--where "location" like '%Para%'
where continent  is not null 
--group by "date" 
order by 1,2

--Looking at Total Population vs Vaccinations
with PopvsVac as (
select c.continent , c."location" , c."date" , c.population ,
c2.new_vaccinations , 
sum(c2.new_vaccinations) over (partition by c."location" order by c."location" ,c."date") as RollingPeopleVaccinated
from coviddeaths c 
join covidvaccinations c2 
	on c."location"  = c2."location" 
	and c."date" =c2."date" 
where c.continent  is not null 
--order by 2,3
)
select *, (rollingpeoplevaccinated/population)*100
from PopvsVac

--TEMP TABLE 
drop table if exists PercentPopulationVaccinated
--
create table PercentPopulationVaccinated 
(
Continent varchar(255),
location varchar(255),
"date" date,
Population bigint,
New_Vaccinations float8,
RollingPeopleVaccinated numeric)

insert into PercentPopulationVaccinated
select c.continent , c."location" , c."date" , c.population ,
c2.new_vaccinations , 
sum(c2.new_vaccinations) over (partition by c."location" order by c."location" ,c."date") as RollingPeopleVaccinated
from coviddeaths c 
join covidvaccinations c2 
	on c."location"  = c2."location" 
	and c."date" =c2."date" 
where c.continent  is not null 





